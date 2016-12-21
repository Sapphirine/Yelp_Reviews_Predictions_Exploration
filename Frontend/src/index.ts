import * as express from 'express';

var app = express();

app.use(express.static('www'));

app.listen(3000, () => {
    console.log('App is listening on port 3000!');
});