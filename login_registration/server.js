var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/mongoose_pack');
var session = require('express-session');
app.set('trust proxy', 1) // trust first proxy
app.use(session({
 secret: 'keyboard cat',
 resave: false,
 saveUninitialized: true,
 cookie: { maxAge: 60000 }
}));

app.get('/',function(req,res){
	res.render('index')
})

app.listen(8000, function() {
    console.log("listening on port 8000");
})
