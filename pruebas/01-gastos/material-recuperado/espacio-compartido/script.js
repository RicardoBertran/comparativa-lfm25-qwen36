// Control de Gastos Personales - Lógica principal

const STORAGE_KEY = 'expense_transactions';
let transactions = [];

function loadTransactions() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
        try {
            const parsed = JSON.parse(stored);
            if (Array.isArray(parsed) && parsed.length > 0) {
                transactions = parsed;
                return;
            }
        } catch (e) {
            // Si la carga falla, usar datos de ejemplo
        }
    }
    // Datos de ejemplo (8 transacciones)
    transactions = [
        {id: 1, date: "2025-01-01", description: "Salario mensual", amount: 3000, type: "income"},
        {id: 2, date: "2025-01-05", description: "Alquiler", amount: 1200, type: "expense"},
        {id: 3, date: "2025-01-10", description: "Compras de supermercado", amount: 200, type: "expense"},
        {id: 4, date: "2025-01-12", description: "Servicios públicos", amount: 100, type: "expense"},
        {id: 5, date: "2025-01-15", description: "Trabajo freelance", amount: 500, type: "income"},
        {id: 6, date: "2025-01-18", description: "Transporte", amount: 50, type: "expense"},
        {id: 7, date: "2025-01-20", description: "Entretenimiento", amount: 80, type: "expense"},
        {id: 8, date: "2025-01-22", description: "Ropa", amount: 150, type: "expense"}
    ];
}

function saveTransactions() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(transactions));
}

function getIncome() {
    return transactions.filter(t => t.type === 'income').reduce((sum, t) => sum + t.amount, 0);
}

function getExpenses() {
    return transactions.filter(t => t.type === 'expense').reduce((sum, t) => sum + t.amount, 0);
}

function getBalance() {
    return getIncome() - getExpenses();
}

function renderStats() {
    const income = getIncome();
    const expenses = getExpenses();
    const balance = getBalance();
    document.getElementById('balance').textContent = '$' + balance.toFixed(2);
    document.getElementById('income').textContent = '$' + income.toFixed(2);
    document.getElementById('expense').textContent = '$' + expenses.toFixed(2);
}

function getExpenseCategories() {
    const categories = {};
    transactions.filter(t => t.type === 'expense').forEach(t => {
        let cat;
        const desc = t.description.toLowerCase();
        if (desc.includes('alquiler')) cat = 'Vivienda';
        else if (desc.includes('supermercado') || desc.includes('compras')) cat = 'Supermercados';
        else if (desc.includes('servicios') || desc.includes('utilities')) cat = 'Servicios';
        else if (desc.includes('transporte')) cat = 'Transporte';
        else if (desc.includes('entretenimiento')) cat = 'Entretenimiento';
        else if (desc.includes('ropa')) cat = 'Ropa';
        else cat = 'Otro';
        categories[cat] = (categories[cat] || 0) + t.amount;
    });
    return Object.entries(categories).map(([name, amount]) => ({name, amount}));
}

function renderChart() {
    const svg = document.getElementById('expense-chart');
    svg.innerHTML = '';
    const categories = getExpenseCategories();
    if (categories.length === 0) return;
    const maxVal = Math.max(...categories.map(c => c.amount), 1);
    const chartHeight = 200;
    const barWidth = 60;
    const gap = 20;
    let offsetX = 40;

    categories.forEach(cat => {
        const barHeight = (cat.amount / maxVal) * chartHeight;
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', offsetX);
        rect.setAttribute('y', chartHeight - barHeight);
        rect.setAttribute('width', barWidth);
        rect.setAttribute('height', barHeight);
        rect.setAttribute('fill', '#00c853');
        svg.appendChild(rect);

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', offsetX + barWidth / 2);
        text.setAttribute('y', chartHeight - barHeight / 2 + 4);
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('fill', '#000');
        text.setAttribute('font-size', '12');
        text.textContent = cat.name + ': $' + cat.amount;
        svg.appendChild(text);

        offsetX += barWidth + gap;
    });
}

function renderTransactions() {
    const tbody = document.getElementById('transactions-body');
    tbody.innerHTML = '';
    transactions.forEach(t => {
        const tr = document.createElement('tr');
        const date = new Date(t.date).toLocaleDateString('es-ES', {day: '2-digit', month: 'short', year: 'numeric'});
        const typeClass = t.type === 'income' ? 'income' : 'expense';
        tr.innerHTML = `<td>${date}</td><td>${t.description}</td><td><span class="type-badge ${typeClass}">${t.type}</span></td><td>$${t.amount.toFixed(2)}</td>`;
        tbody.appendChild(tr);
    });
}

function addTransaction(data) {
    const newId = transactions.length > 0 ? Math.max(...transactions.map(t => t.id)) + 1 : 1;
    const transaction = {...data, id: newId};
    transactions.push(transaction);
    saveTransactions();
    renderStats();
    renderChart();
    renderTransactions();
}

document.getElementById('add-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const type = document.getElementById('type').value;
    const description = document.getElementById('description').value.trim();
    const amount = parseFloat(document.getElementById('amount').value);
    if (!description || isNaN(amount) || amount <= 0) return;
    addTransaction({description, amount, type});
    this.reset();
});

// Inicialización
loadTransactions();
renderStats();
renderChart();
renderTransactions();
