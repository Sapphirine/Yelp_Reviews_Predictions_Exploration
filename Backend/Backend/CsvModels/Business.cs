using System;
namespace Backend.CsvModels
{
    public class Business
    {
        public string business_id
        {
            get;
            set;
        }

        public decimal latitude
        {
            get;
            set;
        }

        public decimal longitude
        {
            get;
            set;
        }

        public string business_name
        {
            get;
            set;
        }
    }
}
