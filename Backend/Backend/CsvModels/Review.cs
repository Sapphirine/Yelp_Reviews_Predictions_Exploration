using System;
namespace Backend.CsvModels
{
    public class Review
    {
        public string restaurant_name
        {
            get;
            set;
        }

        public string review_id
        {
            get;
            set;
        }

        public string text
        {
            get;
            set;
        }

        public decimal polarity
        {
            get;
            set;
        }
    }
}
