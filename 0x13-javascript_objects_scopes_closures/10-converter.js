#!/usr/bin/node
exports.converter = function (base) {
  if (base <= 1) return;

  this.converter = function (number) {
    if (number >= base) {
      this.converter(number / base);
    }
    process.stdout.write(String(number % base));
  };
};
