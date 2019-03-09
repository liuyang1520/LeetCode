const util = require('util')
const gulp = require('gulp');
const tap = require('gulp-tap');

exports.stats = (cb) => {
  let difficulty = {
    easy: 0,
    medium: 0,
    hard: 0
  }, tags = {};
  let regex = /^"""\s@difficulty:\s([\s\S]*?)\n@tags:\s([\s\S]*?)\n@notes:\s([\s\S]*?)\n"""/;

  return gulp.src('solution/python/*.py')
    .pipe(tap((file, t) => {
      content = file.contents.toString();
      metadata = content.match(regex);
      if (metadata == null) return;
      if (difficulty.hasOwnProperty(metadata[1])) {
        difficulty[metadata[1]] += 1;
      }
      tags[file.basename] = metadata[2];
    }).on('finish', () => {
      console.log(difficulty);
      console.log(tags);
    })
  )
};
