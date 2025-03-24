const express = require('express');
const router = express.Router();
const axios = require('axios');

// Rota para buscar produtos
router.get('/products', async (req, res) => {
  try {
    const response = await axios.get('http://localhost:5000/api/products');
    res.json(response.data);
  } catch (error) {
    res.status(500).send('Erro ao buscar produtos');
  }
});

module.exports = router;