const express = require('express')
const bodyParser = require('body-parser')

const app = express()

app.use(bodyParser.json())

const port = 3000

app.post('/api', (req, res) => {
  // get the name from the request body
  const name = req.body.name
  res.json({ message: `Hello ${name}!` })
})

app.listen(port, () => {
  console.log(`Server listening on port ${port}`)
})
