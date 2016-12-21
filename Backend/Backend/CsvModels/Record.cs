using System;
namespace Backend.CsvModels
{
    public class Record
    {
        public string name
        {
            get;
            set;
        }

        public string word
        {
            get;
            set;
        }

        public int count
        {
            get;
            set;
        }

        public int positive
        {
            get;
            set;
        }

        public int negative
        {
            get;
            set;
        }

        public string review_ids
        {
            get;
            set;
        }
    }
}
