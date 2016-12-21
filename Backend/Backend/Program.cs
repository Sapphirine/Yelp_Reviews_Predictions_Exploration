using System;
using System.Linq;
using Dapper;
using Mono.Data.Sqlite;
using Nancy;
using Nancy.Hosting.Self;
using Backend.Models;

namespace Backend
{
    public class MainClass : NancyModule
    {
        const string _connString = @"Data Source=data.db";
        readonly SqliteConnection _db = new SqliteConnection(_connString);

        public MainClass()
        {
            StaticConfiguration.DisableErrorTraces = false;

            Get["/"] = _ => "Hello Big Data!";

            Get["/restaurants"] = _ =>
            {
                return Response.AsJson(_db.Query<Business>("SELECT * FROM Business")
                                       .Select(b => new
                                       {
                                           Address = $"[{b.Lat}, {b.Lon}]",
                                           b.Name,
                                           b.Id
                                       }));
            };

            Get["/restaurants/{id}/name"] = _ =>
            {
                var id = (string)_.id;
                Console.WriteLine(id);

                return _db.Query<string>("SELECT Name FROM Business WHERE Id = @Id", new { Id = id }).FirstOrDefault();
            };

            Get["/restaurants/{id}/info"] = _ =>
            {
                var id = (string)_.id;
                Console.WriteLine(id);

                return Response.AsJson(_db.Query<Word>("SELECT * FROM Word WHERE BusinessId = @Id", new { Id = id })
                                       .Take(50)
                                       .Select((w, i) => new
                                       {
                                           Name = w.Name.Split(' ')[0],
                                           Id = $"i{i}",
                                           w.Positive,
                                           w.Negative,
                                           w.Count
                                       }));
            };

            Get["/restaurants/{id}/reviews"] = _ =>
            {
                var id = (string)_.id;
                Console.WriteLine(id);

                return Response.AsJson(_db.Query<Word>("SELECT * FROM Word WHERE BusinessId = @Id", new { Id = id })
                                       .SelectMany(w => w.GetReviewIds())
                                       .Distinct()
                                       .Select((i, n) =>
                                       {
                                           var review = _db.Query<Review>("SELECT * FROM Review WHERE Id = @Id", new { Id = i }).FirstOrDefault();
                                           return new
                                           {
                                               review.Content,
                                               Polarity = Math.Round(review.Polarity, 3),
                                               Id = $"r{n}"
                                           };
                                       }));
            };
        }

        public static void Main(string[] args)
        {
            using (var host = new NancyHost(new Uri("http://localhost:5000")))
            {
                host.Start();
                Console.WriteLine("Running... on port 5000");
                Console.ReadLine();
            }
        }
    }
}
