function GroceryShoppingList() {
  const [groceryItem, setGroceryItem] = useState("");
  const [items, setItems] = useState<string[]>([]);

  const addNewItemToShoppingList = useCallback(() => {
    setItems([groceryItem, ...items]);
    setGroceryItem("");
  }, [groceryItem, items]);

  return (
    <>
      <TextInput
        value={groceryItem}
        placeholder="Enter grocery item"
        onChangeText={(text) => setGroceryItem(text)}
      />
      <Button title="Add the item to list" onPress={addNewItemToShoppingList} />
      {items.map((item) => (
        <Text key={item}>{item}</Text>
      ))}
    </>
  );
}
