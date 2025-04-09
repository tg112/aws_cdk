fetch('https://y5i0oqr470.execute-api.ap-northeast-1.amazonaws.com/prod/employees?id=2b727c49-0bbe-4abd-bae2-ee5744f4d3cb', {
    method: "GET"
}).then(res => res.json())
    .then(res => console.log(res))