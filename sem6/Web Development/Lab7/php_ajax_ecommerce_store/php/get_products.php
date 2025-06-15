<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
require 'db.php';
if (!$pdo) {
    die("DB connection failed");
}
$category = $_GET['category'];
$page = $_GET['page'];
$limit = 4;
$offset = ($page - 1) * $limit;

$stmt = $pdo->prepare("SELECT * FROM products WHERE category_id = ? LIMIT ? OFFSET ?");
$stmt->execute([$category, $limit, $offset]);
echo json_encode($stmt->fetchAll());
?>