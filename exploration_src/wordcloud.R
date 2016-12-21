library(wordcloud)
for (star in 1:5) {
  data = read.csv(paste('/Users/zhi/Desktop/Yelp/review_new', '/', 'uk-review-', star, '.csv', sep=''))
  png(paste('/Users/zhi/Desktop/Yelp/wordcloud_output', '/', 'uk-', star, '.png', sep=''), width=1024, height=1024)
  wordcloud(data$word, data$freq, scale=c(5,0.5), max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, "Dark2"))
  dev.off()
}

for (star in 1:5) {
  data = read.csv(paste('/Users/zhi/Desktop/Yelp/review_new', '/', 'can-review-', star, '.csv', sep=''))
  png(paste('/Users/zhi/Desktop/Yelp/wordcloud_output', '/', 'can-', star, '.png', sep=''), width=1024, height=1024)
  wordcloud(data$word, data$freq, scale=c(5,0.5), max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, "Dark2"))
  dev.off()
}

for (star in 1:5) {
  data = read.csv(paste('/Users/zhi/Desktop/Yelp/review_new', '/', 'usa-review-', star, '.csv', sep=''))
  png(paste('/Users/zhi/Desktop/Yelp/wordcloud_output', '/', 'usa-', star, '.png', sep=''), width=1024, height=1024)
  wordcloud(data$word, data$freq, scale=c(5,0.5), max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, "Dark2"))
  dev.off()
}

for (star in 1:5) {
  data = read.csv(paste('/Users/zhi/Desktop/Yelp/review_new', '/', 'ger-review-', star, '.csv', sep=''))
  png(paste('/Users/zhi/Desktop/Yelp/wordcloud_output', '/', 'ger-', star, '.png', sep=''), width=1024, height=1024)
  wordcloud(data$word, data$freq, scale=c(5,0.5), max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, "Dark2"))
  dev.off()
}