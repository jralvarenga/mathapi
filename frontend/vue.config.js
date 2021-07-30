const path = require('path');

module.exports = {
  publicPath: '/static/', // Should be STATIC_URL + path/to/build
  outputDir: path.resolve(__dirname, '../static/'), // Output to a directory in STATICFILES_DIRS
  filenameHashing: false,
  runtimeCompiler: true,
  devServer: {
    writeToDisk: true,
  },
};