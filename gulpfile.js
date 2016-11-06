// requirements
var gulp = require('gulp');
var gulpBrowser = require("gulp-browser");
var del = require('del');
var size = require('gulp-size');
var sass = require('gulp-sass');

// tasks
gulp.task('sass', function () {
  return gulp.src('./app/static/sass/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./app/static/css'));
});

gulp.task('del', function () {
  return del(['./app/static/css/main.css']);
});

gulp.task('default', ['del'], function () {
  gulp.start('sass');
  gulp.watch('./sass/**/*.scss', ['sass']);
});
