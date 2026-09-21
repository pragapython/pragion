# Frontend and Backend Separation

Pragion has two explicit application layers.

| Responsibility | Backend | Frontend |
| --- | --- | --- |
| Business logic | Yes | No |
| Database and ORM | Yes | No |
| Authentication and security policy | Yes | UI only |
| REST/JSON API | Yes | Consume |
| HTML structure | No | Yes |
| CSS and visual design | No | Yes |
| DOM and UI interaction | No | Yes |
| Authoritative validation | Yes | No |
| Basic form feedback | No | Yes |

Python owns application behavior and data. HTML owns structure, CSS owns visual design, and JavaScript owns presentation behavior. Neither side reaches directly into the other implementation.
