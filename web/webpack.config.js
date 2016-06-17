const path = require('path')
const webpack = require('webpack')
const autoprefixer = require('autoprefixer')
const ExtractText = require('extract-text-webpack-plugin')

const extractStyles = new ExtractText('[name].css')

module.exports = {
  entry: [
    '.'
  ],
  output: {
    path: path.resolve('./dist'),
    publicPath: '/dist/',
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
      }, {
        test: /\.sass$/,
        include: path.resolve('./src'),
        loader: extractStyles.extract([
          'css?modules&camelCase&sourceMap',
          'postcss?sourceMap',
          'sass?sourceMap'
        ]),
      }, {
        test: /\.svg$/,
        loader: 'file',
        query: {
          mimetype: 'image/svg+xml'
        }
      }, {
        test: /\.woff$/,
        loader: 'file',
        query: {
          mimetype: 'application/font-woff'
        }
      }, {
        test: /\.woff2$/,
        loader: 'file',
        query: {
          mimetype: 'application/font-woff2'
        }
      }, {
        test: /\.[ot]tf$/,
        loader: 'file',
        query: {
          mimetype: 'application/octet-stream'
        }
      }, {
        test: /\.eot$/,
        loader: 'file',
        query: {
          mimetype: 'application/vnd.ms-fontobject'
        }
      }
    ]
  },
  babel: {
    presets: ['react'],
    plugins: ['transform-es2015-modules-commonjs']
  },
  postcss: function() {
    return [autoprefixer]
  },
  devtool: 'source-map-inline',
  plugins: [
    extractStyles
  ]
}
