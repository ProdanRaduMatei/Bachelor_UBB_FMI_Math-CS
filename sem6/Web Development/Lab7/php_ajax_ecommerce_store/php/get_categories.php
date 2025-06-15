<?php
require 'db.php';
$stmt = $pdo->query("SELECT id, name FROM categories");
echo json_encode($stmt->fetchAll());
?>