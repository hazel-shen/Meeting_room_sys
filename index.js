"use strict"
const config = require('dotenv').config();
const express = require('express')
const path = require('path')
const axios = require('axios')
const bodyParser = require('body-parser')
const history = require('connect-history-api-fallback')
const app = express()
const staticFileMiddleware = express.static(path.join(__dirname + '/dist'))
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json())
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*") // Should be fixed before Risk assessment
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  )
  next()    
})
app.use(staticFileMiddleware)
app.get('/', (req, res) => {
  res.sendStatus(200).render(path.join(__dirname + '/dist/index.html'))
})


app.listen(process.env.PORT || 8000)
