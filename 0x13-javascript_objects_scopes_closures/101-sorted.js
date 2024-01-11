#!/usr/bin/node

const { dict } = require('./101-data');

const occurrencesByUsers = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (occurrencesByUsers[occurrences] === undefined) {
    occurrencesByUsers[occurrences] = [];
  }

  occurrencesByUsers[occurrences].push(userId.toString());
}

console.log(occurrencesByUsers);
