/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
        './app/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    theme: {
        extend: {
            animation: {
                'gradient-x': 'gradient-x 25s ease-in-out infinite',
            },
            keyframes: {
                'gradient-x': {
                    '0%, 100%': {
                        'background-size': '300% 300%',
                        'background-position': 'left center'
                    },
                    '50%': {
                        'background-size': '300% 300%',
                        'background-position': 'right center'
                    },
                },
            },
        },
    },
    plugins: [],
} 