module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/essential',
    'eslint:recommended'
  ],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    'vue/no-parsing-error': [2, { "x-invalid-end-tag": false }],
    'no-unused-vars':0,
    "no-console": "off"
  }
}