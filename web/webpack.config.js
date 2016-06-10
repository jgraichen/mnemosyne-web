const path = require('path')
const webpack = require('webpack')

module.exports = {
  entry: [
    '.'
  ],
  output: {
    path: path.resolve('./dist'),
    publicPath: '/dist',
    filename: '[name].js',
  },
  resolve: {
    alias: {
      'react': path.resolve('./node_modules/react')
    },
    extensions: ['', '.js', '.jsx']
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        include: path.resolve('./src'),
        loaders: ['react-hot', 'babel'],
      }
    ]
  },
  babel: {
    presets: ['react'],
    plugins: ['transform-es2015-modules-commonjs']
  },
  devtool: 'source-map-inline'
}
