using System;
namespace Backend.Models
{
    public class Review
    {
        public string Id
        {
            get;
            set;
        }

        public string Content
        {
            get;
            set;
        }

        public decimal Polarity
        {
            get;
            set;
        }
    }
}
