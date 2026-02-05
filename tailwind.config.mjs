/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./node_modules/flowbite/**/*.js",
        './src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'
    ],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                primary: "#0074d4",
                secondary: "#475569",
                info: "#0C63E7",
                gray: {
                    50: "#FAFAFC",
                    100: "#E9E9EC",
                    200: "#C6C8CD",
                    300: "#ACAEB6",
                    400: "#92959F",
                    500: "#777C87",
                    600: "#5D6370",
                    700: "#434959",
                    800: "#293041",
                    900: "#0f172a",
                },
            },
            fontFamily: {
                sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
                heading: ['Raleway', 'sans-serif'],
            },
        },
    },
    plugins: [
        require('flowbite/plugin'),
        require('@tailwindcss/typography'),
    ],
}

