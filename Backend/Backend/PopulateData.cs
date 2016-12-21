using System;
using Dapper;
using Mono.Data.Sqlite;
using CsvHelper;
using System.IO;
using Backend.CsvModels;

namespace Backend
{
    public static class PopulateData
    {
        const string _connString = @"Data Source=data.db";

        public static void Populate()
        {
            using (var db = new SqliteConnection(_connString))
            {
                db.Open();

                var reviewFile = new StreamReader("bda/review.csv");
                var reviewcsv = new CsvReader(reviewFile);

                var reviews = reviewcsv.GetRecords<Review>();

                foreach (var review in reviews)
                {
                    db.Execute("INSERT INTO Review (Id, Content, Polarity) VALUES (@Id, @C, @P)", new { Id = review.review_id, C = review.text, P = review.polarity });
                }

                var businessFile = new StreamReader("bda/business.csv");
                var businesscsv = new CsvReader(businessFile);

                var businesses = businesscsv.GetRecords<Business>();

                foreach (var business in businesses)
                {
                    db.Execute("INSERT INTO Business (Id, Name, Lon, Lat) VALUES (@Id, @N, @Lon, @Lat)", new { Id = business.business_id, N = business.business_name, Lon = business.longitude, Lat = business.latitude });

                    Console.WriteLine(business.business_id);
                    var recordcsv = GetRecord(business.business_id);
                    var records = recordcsv.GetRecords<Record>();
                    foreach (var record in records)
                    {
                        db.Execute("INSERT INTO Word (BusinessId, Name, Count, Positive, Negative, ReviewIds) VALUES (@Id, @Name, @C, @P, @N, @R)", new { Id = business.business_id, Name = record.name, C = record.count, P = record.positive, N = record.negative, R = record.review_ids });
                    }
                }

                db.Close();
            }
        }

        static CsvReader GetRecord(string name)
        {
            var recordFile = new StreamReader("bda/output/" + name + ".csv");
            return new CsvReader(recordFile);
        }
    }
}
