const express = require('express');
const path = require('path');
const bcrypt = require('bcrypt');
const cors = require("cors");
const app = express();

app.use(express.json()); 
app.use(express.static(path.join(__dirname, 'Front-End')));
app.use(cors());


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'Front-End', 'index.html'));
});

app.post('/hash', (req, res) => {
    const data = req.body;
    bcrypt.hash(data.pass,10,function(err,hash) {
        res.send(hash);
    })
});

app.post('/sign', (req, res) => {
    const data = req.body;
    bcrypt.compare(data.contrasena, data.hash, function(err, result) {
        res.send(result);
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
