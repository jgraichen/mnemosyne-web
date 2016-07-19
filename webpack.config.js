const path = require('path')
const webpack = require('webpack')
const autoprefixer = require('autoprefixer')
const webpackNotifier = require('webpack-notifier');

module.exports = {
  // entry: ['babel-regenerator-runtime', path.resolve('./web/index.js')],
  entry: [
    path.resolve('./web/index.js')
  ],
  output: {
    path: path.resolve('./public/assets'),
    publicPath: '/assets/',
    filename: '[name].js',
  },
  resolve: {
    alias: {
      'react': path.dirname(require.resolve('react'))
    },
    extensions: ['', '.js', '.jsx']
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        include: path.resolve('./web'),
        loaders: ['react-hot', 'babel?presets[]=es2015&presets[]=stage-0&presets[]=react'],
      }, {
        test: /\.css$/,
        loader: "style-loader!css-loader"
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
    presets: [
      'react', 'stage-2'
    ],
    plugins: [
      'syntax-class-properties',
      'transform-es2015-modules-commonjs',
      'transform-class-properties'
    ]
  },
  postcss: function() {
    return [autoprefixer]
  },
  plugins: [
    new webpackNotifier()
  ],
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
