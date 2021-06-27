const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
// const HtmlWebpackPlugin = require('html-webpack-plugin');
const { WebpackManifestPlugin } = require('webpack-manifest-plugin'); //https://github.com/shellscape/webpack-manifest-plugin


module.exports = (env) => {
    const isProd = env.production;

    return {
        mode: isProd ? 'production' : 'development',
        entry: './src/index.js',
        output: {
            filename: 'main.[contenthash].js',
            path: path.resolve(__dirname, '../public/dist'),
            clean: true,
            publicPath: "",
        },
        plugins: [
            new WebpackManifestPlugin({
                publicPath: "dist/"
            }),
            new MiniCssExtractPlugin({filename: '[name].[contenthash].css',}),
            // new HtmlWebpackPlugin()
        ],
        module: {
            rules: [
                {
                    test: /\.css$/i,
                    use: [
                        MiniCssExtractPlugin.loader,
                        'css-loader'
                    ],
                },
                {
                    test: /\.(scss)$/,
                    use: [
                        MiniCssExtractPlugin.loader,
                        'css-loader',
                        'sass-loader'
                    ],
                },
            ],
        },
        optimization: {
            minimizer: [
                `...`,
                new CssMinimizerPlugin(),
            ],
        },
    };
}
