using System;
using Newtonsoft.Json;
namespace Backend.Models
{
    public class Word
    {
        public int RowId
        {
            get;
            set;
        }

        public string BusinessId
        {
            get;
            set;
        }

        public string Name
        {
            get;
            set;
        }

        public int Count
        {
            get;
            set;
        }

        public int Positive
        {
            get;
            set;
        }

        public int Negative
        {
            get;
            set;
        }

        public string ReviewIds
        {
            get;
            set;
        }

        public string[] GetReviewIds()
        {
            return JsonConvert.DeserializeObject<string[]>(ReviewIds);
        }

        public void SetReviewIds(string[] ids)
        {
            ReviewIds = JsonConvert.SerializeObject(ids);
        }
    }
}
