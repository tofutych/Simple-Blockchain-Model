# Элементарная программная реализация цепочки из блоков

> Создание генезис-блока
>
> ```python
> blockchain.genesis_block()
> ```

> Испорт данных из csv
>
> ```python
> blockchain.from_csv("transactions.csv")
> ```

> Добавление блока вручную
>
> ```python
> blockchain.add_block(["A", "B", "6BTC"])
> ```

> Проверка цепочки на целостность
>
> ```python
> blockchain.check_integrity()
> ```

---

Блоки сохраняются в папку Blocks

Результат проверки на целостность сохраняется в файл valid.json
