const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors()); // Enable CORS

app.use(bodyParser.json());

app.post('/data', (req, res) => {
  console.log('Received POST request with data:', req.body);
  res.json({ message: 'Data received successfully!' });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
