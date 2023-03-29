import * as redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

const channel = 'holberton school channel';

subscriber.subscribe(channel, (err) => {
  if (err) {
    console.log(`Redis client could not subscribe to the channel: ${err}`);
  }
});

subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(`${channel}`);
    subscriber.quit();
  }
});
