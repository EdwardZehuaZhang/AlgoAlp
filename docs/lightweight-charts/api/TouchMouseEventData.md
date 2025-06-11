# API: Touchmouseeventdata

*Source: docs\api\interfaces\TouchMouseEventData.html*

Version: 5.0

On this page

The TouchMouseEventData interface represents events that occur due to the user interacting with a pointing device (such as a mouse). See [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)

## Properties[​](TouchMouseEventData.html#properties "Direct link to Properties")

### clientX[​](TouchMouseEventData.html#clientx "Direct link to clientX")

> `readonly` **clientX** : [`Coordinate`](../type-aliases/Coordinate.md)

The X coordinate of the mouse pointer in local (DOM content) coordinates.

* * *

### clientY[​](TouchMouseEventData.html#clienty "Direct link to clientY")

> `readonly` **clientY** : [`Coordinate`](../type-aliases/Coordinate.md)

The Y coordinate of the mouse pointer in local (DOM content) coordinates.

* * *

### pageX[​](TouchMouseEventData.html#pagex "Direct link to pageX")

> `readonly` **pageX** : [`Coordinate`](../type-aliases/Coordinate.md)

The X coordinate of the mouse pointer relative to the whole document.

* * *

### pageY[​](TouchMouseEventData.html#pagey "Direct link to pageY")

> `readonly` **pageY** : [`Coordinate`](../type-aliases/Coordinate.md)

The Y coordinate of the mouse pointer relative to the whole document.

* * *

### screenX[​](TouchMouseEventData.html#screenx "Direct link to screenX")

> `readonly` **screenX** : [`Coordinate`](../type-aliases/Coordinate.md)

The X coordinate of the mouse pointer in global (screen) coordinates.

* * *

### screenY[​](TouchMouseEventData.html#screeny "Direct link to screenY")

> `readonly` **screenY** : [`Coordinate`](../type-aliases/Coordinate.md)

The Y coordinate of the mouse pointer in global (screen) coordinates.

* * *

### localX[​](TouchMouseEventData.html#localx "Direct link to localX")

> `readonly` **localX** : [`Coordinate`](../type-aliases/Coordinate.md)

The X coordinate of the mouse pointer relative to the chart / price axis / time axis canvas element.

* * *

### localY[​](TouchMouseEventData.html#localy "Direct link to localY")

> `readonly` **localY** : [`Coordinate`](../type-aliases/Coordinate.md)

The Y coordinate of the mouse pointer relative to the chart / price axis / time axis canvas element.

* * *

### ctrlKey[​](TouchMouseEventData.html#ctrlkey "Direct link to ctrlKey")

> `readonly` **ctrlKey** : `boolean`

Returns a boolean value that is true if the Ctrl key was active when the key event was generated.

* * *

### altKey[​](TouchMouseEventData.html#altkey "Direct link to altKey")

> `readonly` **altKey** : `boolean`

Returns a boolean value that is true if the Alt (Option or ⌥ on macOS) key was active when the key event was generated.

* * *

### shiftKey[​](TouchMouseEventData.html#shiftkey "Direct link to shiftKey")

> `readonly` **shiftKey** : `boolean`

Returns a boolean value that is true if the Shift key was active when the key event was generated.

* * *

### metaKey[​](TouchMouseEventData.html#metakey "Direct link to metaKey")

> `readonly` **metaKey** : `boolean`

Returns a boolean value that is true if the Meta key (on Mac keyboards, the ⌘ Command key; on Windows keyboards, the Windows key (⊞)) was active when the key event was generated.
