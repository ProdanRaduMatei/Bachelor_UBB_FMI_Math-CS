<?php
require 'db.php';
session_start();
$cart = $_SESSION['cart'] ?? [];
$inClause = implode(',', array_fill(0, count($cart), '?'));

if (count($cart) > 0) {
    $stmt = $pdo->prepare("SELECT * FROM products WHERE id IN ($inClause)");
    $stmt->execute($cart);
    echo json_encode($stmt->fetchAll());
} else {
    echo json_encode([]);
}
?>