const path = require('path');

module.exports ={
    entry: './src/index.js',
    outtput: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
    },
    resolve:{
        extensions: ['.js','.jsx'],
    }
    
}