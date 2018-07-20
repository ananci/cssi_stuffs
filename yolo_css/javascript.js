console.log('Hello World!');

const name = 'Charlie';
console.log(`Hello ${name}!`);

const age = 20;
console.log(`You are ${age} years old!`);

// line comment
/*
 * block comment
 * multiple lines
 */
/**
 * documentation
 */

if (age >= 18) {
  console.log('You can get your driver\'s permit and vote.');
} else if (age < 15) {
  console.log('You will have to wait to get your permit and cannot vote.');
} else {
  console.log('You can get your permit but you cannot vote.');
}

function makeGreetingMessage(name1, name2=null) {
  if (name2 == null) {
    return `Hello ${name1}.`;
  } else {
    // code
    return `Hello ${name1} and ${name2}`;
  }
}

function greet(name1, name2=null) {
  if (name1[0] !== 'A') {
    return;
  }
  console.log(makeGreetingMessage(name1, name2));
}

greet('Alice', 'Bob');

const multiplyBy3 = (x) => x * 3;
console.log(multiplyBy3(3));

let n = 0;
// setInterval(() => {
//   n += 1;
//   console.log(n);
// }, 1000);

const multiplyBy4 = function (x) {
  return x * 3;
};

document.addEventListener('DOMContentLoaded', () => {
  const likeButton = document.querySelector('.likeButton');
  likeButton.addEventListener('click', () => {
    const greetingMessage = makeGreetingMessage('Alice');
    likeButton.innerText = greetingMessage;
    likeButton.style.backgroundColor = 'blue';
  });
});

const names = ['Alice', 'Bob', 'Charlie'];
for (let i = 0; i < names.length; i++) {
  console.log(names[i]);
  console.log(names[i]);
}

// let i = 0;
// // is i < 4 === true <--beginning
// console.log(names[i]);
// console.log(names[i]);
// i++ // i = 1
// // is i < 4 === true
// console.log(names[i]);
// console.log(names[i]);
// i++ // i = 2
// console.log(names[i]);
// console.log(names[i]);
// i++ // i = 3
// console.log(names[i]);
// console.log(names[i]);
// i++ // i = 4
// // is i < 4 === false

let count = 0;
while (count < 4) {
  count++;
  console.log(count);
}

names.forEach((name) => {
  console.log(`forEach: ${name}`);
});

const article = {
  name: 'Dog family gives birth to litter of 10 puppies',
  views: 1234,
  datePublished: '03/25/2018',
  author: {
    name: 'Joe Corgi',
    title: 'Senior Canine Editor',
  },
  editors: [{
    name: '...',
    title: '...'
  }, {
    name: '...',
    title: '...',
  }],
};

document.addEventListener('DOMContentLoaded', () => {
  const floatingBox = document.querySelector('.floatingBox');
  let boxTop = 100;
  let boxLeft = 100;
  document.addEventListener('keydown', (event) => {
    const key = event.key;
    if (key === 'ArrowDown') {
      boxTop += 5;
    } else if (key === 'ArrowUp') {
      boxTop -= 5;
    } else if (key === 'ArrowLeft') {
      boxLeft -= 5;
    } else if (key === 'ArrowRight') {
      boxLeft += 5;
    } else {
      return;
    }
    floatingBox.style.top = boxTop + 'px';
    floatingBox.style.left = boxLeft + 'px';
    console.log(event);
  });
}); 
