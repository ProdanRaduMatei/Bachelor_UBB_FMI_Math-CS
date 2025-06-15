let currentPage = 1;
let selectedCategory = "";

function loadCategories() {
    fetch('php/get_categories.php')
        .then(res => res.json())
        .then(categories => {
            const select = document.getElementById('categorySelect');
            categories.forEach(cat => {
                const option = document.createElement('option');
                option.value = cat.id;
                option.textContent = cat.name;
                select.appendChild(option);
            });
            selectedCategory = select.value;
            loadProducts();
        });
}

function loadProducts() {
    fetch(`php/get_products.php?category=${selectedCategory}&page=${currentPage}`)
        .then(res => res.json())
        .then(products => {
            const list = document.getElementById('productList');
            list.innerHTML = '';
            products.forEach(p => {
                const div = document.createElement('div');
                div.className = 'product';
                div.innerHTML = `<strong>${p.name}</strong><br>Price: $${p.price}<br>
                                 <button onclick="addToCart(${p.id})">Add to Cart</button>`;
                list.appendChild(div);
            });
        });
}

function addToCart(productId) {
    fetch(`php/add_to_cart.php`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: productId })
    }).then(() => loadCart());
}

function loadCart() {
    fetch('php/get_cart.php')
        .then(res => res.json())
        .then(cart => {
            const cartDiv = document.getElementById('cart');
            cartDiv.innerHTML = '';
            cart.forEach(item => {
                const div = document.createElement('div');
                div.className = 'cart-item';
                div.innerHTML = `${item.name} - $${item.price}
                                 <button onclick="removeFromCart(${item.id})">Remove</button>`;
                cartDiv.appendChild(div);
            });
        });
}

function removeFromCart(productId) {
    fetch('php/remove_from_cart.php', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: productId })
    }).then(() => loadCart());
}

document.getElementById('categorySelect').addEventListener('change', (e) => {
    selectedCategory = e.target.value;
    currentPage = 1;
    loadProducts();
});

document.getElementById('prevPage').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        loadProducts();
    }
});

document.getElementById('nextPage').addEventListener('click', () => {
    currentPage++;
    loadProducts();
});

window.onload = () => {
    loadCategories();
    loadCart();
};