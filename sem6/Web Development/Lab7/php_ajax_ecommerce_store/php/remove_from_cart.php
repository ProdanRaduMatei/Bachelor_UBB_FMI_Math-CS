<?php
session_start();
$data = json_decode(file_get_contents('php://input'), true);
$id = $data['id'];
$_SESSION['cart'] = array_filter($_SESSION['cart'], fn($item) => $item != $id);
?>