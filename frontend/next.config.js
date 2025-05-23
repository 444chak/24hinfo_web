/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    async rewrites() {
        return [
            {
                source: '/api/:path*',
                destination: 'http://10.17.40.103:8000/api/:path*',
            },
        ]
    },
}

module.exports = nextConfig 