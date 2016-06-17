const path = require('path')
const webpack = require('webpack')
const autoprefixer = require('autoprefixer')

module.exports = {
  entry: [
    './web/index.js'
  ],
  output: {
    path: path.resolve('./public/assets'),
    publicPath: '/assets/',
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
        include: path.resolve('./web'),
        loaders: ['react-hot', 'babel'],
      }, {
        test: /\.sass$/,
        loaders: [
          'style',
          'css?modules&camelCase',
          'postcss?sourceMap',
          'sass?sourceMap'
        ],
      }, {
        test: /\.svg(\?.*)?$/,
        loader: 'file',
        query: {
          mimetype: 'image/svg+xml'
        }
      }, {
        test: /\.woff(\?.*)?$/,
        loader: 'file',
        query: {
          mimetype: 'application/font-woff'
        }
      }, {
        test: /\.woff2(\?.*)?$/,
        loader: 'file',
        query: {
          mimetype: 'application/font-woff2'
        }
      }, {
        test: /\.[ot]tf(\?.*)?$/,
        loader: 'file',
        query: {
          mimetype: 'application/octet-stream'
        }
      }, {
        test: /\.eot(\?.*)?$/,
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
  devServer: {
    port: 8081,
    inline: true,
    contentBase: path.resolve('./public'),
    proxy: {
      "*": "http://localhost:8080"
    },
  }
}
