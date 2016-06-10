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
        loader: 'babel',
      }
    ]
  },
  babel: {
    presets: ['react']
  },
  devtool: 'source-map-inline',
  devServer: {
    contentBase: path.resolve('./static'),
    inline: true,
  }
}
