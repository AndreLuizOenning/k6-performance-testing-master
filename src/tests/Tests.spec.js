import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 7 },
    { duration: '2m', target: 92 },
    { duration: '1m20s', target: 92 }
  ],

  thresholds: {
    http_req_duration: ['p(90)<6800'],
    http_req_failed: ['rate<0.25']
  }
};

export default function () {
  const url = 'https://httpbin.org/get';

  const res = http.get(url);

  check(res, {
    'status 200': r => r.status === 200,
    'tempo OK': r => r.timings.duration < 1000
  });
  sleep(1);
}
