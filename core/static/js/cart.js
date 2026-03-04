document.addEventListener('DOMContentLoaded', function() {
    const CART_KEY = 'poro_run_cart';
    
    function getCart() {
        try {
            return JSON.parse(localStorage.getItem(CART_KEY)) || [];
        } catch(e) {
            return [];
        }
    }
    
    function saveCart(cart) {
        try {
            localStorage.setItem(CART_KEY, JSON.stringify(cart));
        } catch(e) {
            console.warn('Impossible de sauvegarder le panier');
        }
    }
    
    function updateCartDisplay() {
        const cart = getCart();
        const resumeEl = document.getElementById('resume');
        const totalEl = document.getElementById('total');
        
        if (!resumeEl || !totalEl) return;
        
        if (cart.length === 0) {
            resumeEl.innerHTML = '<p style="color: #9ca3af; text-align: center; padding: 20px;">Votre panier est vide</p>';
            totalEl.textContent = 'Total: 0 FCFA';
            return;
        }
        
        let html = '';
        let total = 0;
        
        cart.forEach((item, index) => {
            const itemTotal = item.price * item.qty;
            total += itemTotal;
            html += `
                <div class="resume-item">
                    <div class="resume-left">
                        <strong>${item.name}</strong>
                    </div>
                    <div class="resume-controls">
                        <button class="btn-small" onclick="updateQty(${index}, -1)">−</button>
                        <span style="padding: 0 10px;">${item.qty}</span>
                        <button class="btn-small" onclick="updateQty(${index}, 1)">+</button>
                    </div>
                    <div class="resume-right">
                        ${itemTotal.toLocaleString()} F
                    </div>
                    <button class="btn-danger" style="margin-left: 8px; padding: 4px 8px;" onclick="removeItem(${index})">×</button>
                </div>
            `;
        });
        
        resumeEl.innerHTML = html;
        totalEl.textContent = `Total: ${total.toLocaleString()}FCFA`;
    }
    
    window.addToCart = function(name, price, qty) {
        const cart = getCart();
        const existing = cart.find(item => item.name === name);
        
        if (existing) {
            existing.qty += qty;
        } else {
            cart.push({ name, price, qty });
        }
        
        saveCart(cart);
        updateCartDisplay();
        showToast(`${qty}x ${name} ajouté au panier!`);
    };
    
    window.updateQty = function(index, delta) {
        const cart = getCart();
        if (cart[index]) {
            cart[index].qty += delta;
            if (cart[index].qty <= 0) {
                cart.splice(index, 1);
            }
            saveCart(cart);
            updateCartDisplay();
        }
    };
    
    window.removeItem = function(index) {
        const cart = getCart();
        cart.splice(index, 1);
        saveCart(cart);
        updateCartDisplay();
    };
    
    window.viderPanier = function() {
        saveCart([]);
        updateCartDisplay();
    };
    
    window.changeQty = function(name, delta) {
        const input = document.querySelector(`input[data-item="${name}"]`);
        if (input) {
            let val = parseInt(input.value) || 0;
            val = Math.max(0, val + delta);
            input.value = val;
        }
    };
    
    function showToast(message) {
        let toast = document.querySelector('.toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.className = 'toast';
            toast.style.cssText = 'position:fixed;right:20px;bottom:20px;background:linear-gradient(135deg,#ff7d00,#ff4da6);color:#fff;padding:14px 24px;border-radius:10px;font-weight:600;z-index:9999;box-shadow:0 8px 24px rgba(0,0,0,0.3);';
            document.body.appendChild(toast);
        }
        toast.textContent = message;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2500);
    }
    
    document.querySelectorAll('.btn-ajouter').forEach(btn => {
        btn.addEventListener('click', function() {
            const name = this.dataset.name;
            const price = parseInt(this.dataset.price);
            const input = document.querySelector(`input[data-item="${name}"]`);
            const qty = input ? parseInt(input.value) || 1 : 1;
            
            if (qty > 0) {
                addToCart(name, price, qty);
            }
        });
    });
    
    updateCartDisplay();
});
