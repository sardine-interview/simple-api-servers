const express = require('express')
const bodyParser = require('body-parser')

const app = express()

app.use(bodyParser.json())

const port = 3000

// This is slow on purpose, don't change it
function fibonacci(n) {
  if (n < 2) return n
  return fibonacci(n - 1) + fibonacci(n - 2)
}

app.get('/fibonacci', (req, res) => {
  const raw = req.query.n

  if (typeof raw !== 'string' || !/^\d+$/.test(raw)) {
    return res.status(400).json({ error: 'n must be an integer between 0 and 50' })
  }

  const n = Number(raw)
  if (n > 50) {
    return res.status(400).json({ error: 'n must be an integer between 0 and 50' })
  }

  res.json({ n, result: fibonacci(n) })
})

app.post('/api', (req, res) => {
  // get the name from the request body
  const name = req.body.name
  res.json({ message: `Hello ${name}!` })
})

app.listen(port, () => {
  console.log(`Server listening on port ${port}`)
})
