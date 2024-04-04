import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import GroceryShoppingList from './GroceryShoppingList';

describe('GroceryShoppingList component', () => {
  test('initial state of groceryItem is an empty string', () => {
    const { getByPlaceholderText } = render(<GroceryShoppingList />);
    const inputElement = getByPlaceholderText('Enter grocery item');
    expect(inputElement.value).toBe('');
  });

  test('initial state of items is an empty array', () => {
    const { container } = render(<GroceryShoppingList />);
    expect(container.querySelectorAll('Text').length).toBe(0);
  });