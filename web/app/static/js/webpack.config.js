var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    context: __dirname,
    // entry point of our app. should require other js modules and dependencies it needs
    entry: [
        'webpack-dev-server/client?http://localhost:8888',
        'webpack/hot/only-dev-server',
        './app.webpack',
    ],
    output: {
      path: path.resolve('./bundles/'),
      filename: "[name]-[hash].js",
      publicPath: 'http://localhost:8888/static/js/bundles/',
    },

    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
        new BundleTracker({filename: './webpack-stats.json'}),
    ],

    module: {
        loaders: [
            {
            test: /\.jsx?$/,
            exclude: /node_modules/,
            loader: ['react-hot-loader', 'babel-loader?presets[]=es2015,presets[]=react'],
            },
        ],
    },

}