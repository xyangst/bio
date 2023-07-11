/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: "#552BFF",
        secondary: "#eb3467",
      },
      fontFamily: {
        sans: ["Poppins", "sans-serif"],
      },
      animation: {
        "fade-in-right": "fade-in-right 1s ease-in-out",
      },
      keyframes: {
        "fade-in-right": {
          "0%": {
            transform: "translateX(4px)",
            opacity: 0,
          },
          "100%": {
            transform: "translateX(0)",
            opacity: 1,
          },
        },
      },
    },
  },
  plugins: [],
};
