/** @type {import('tailwindcss').Config} */
module.exports = {
   content: ["./fastapi_tailwindcss_daisyui_starter/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}

