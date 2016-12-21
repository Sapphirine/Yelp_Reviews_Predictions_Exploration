var gulp = require('gulp');
var typescript = require('gulp-typescript');
var merge2 = require('merge2');
var concat = require('gulp-concat');
var livereload = require('gulp-livereload');

var paths = {
    index: ['./src/index.ts'],
    src: ['./src/www/**/*.ts'],
    output: './www/scripts'
};

gulp.task('default', ['scripts']);

gulp.task('index', function () {
    return gulp.src(paths.index)
        .pipe(typescript({}))
        .js
        .pipe(gulp.dest('./'));
});

gulp.task('scripts', function () {
    var tsResult = gulp.src(paths.src)
        .pipe(typescript({}));

    return merge2([
        tsResult.js
            .pipe(concat('app.all.js'))
            .pipe(gulp.dest(paths.output))
    ]);
});

gulp.task('watch', ['index', 'scripts'], function () {
    livereload.listen();
    gulp.watch(paths.src, ['scripts']);
    gulp.watch(paths.index, ['index']);
});
