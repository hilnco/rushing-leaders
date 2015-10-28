var connectionString = process.env.DATABASE_URL || 'postgres://localhost:5432/stats';

module.exports = connectionString;