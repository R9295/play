var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: {
        polyfill: 'babel-polyfill',
        home:'./play/static/js/index',
        players:'./play/static/js/players',
        profile:'./play/static/js/profile',
        invites:'./play/static/js/invites',
  },

  output: {
      path: path.resolve('./play/static/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }

};
