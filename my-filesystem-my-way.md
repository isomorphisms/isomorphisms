# My filesystem, my way

Filesystems are usually presented as if the machine gets one general answer to storage and every application has to fit itself into it.

I don't see why.

If one application is taking in data quickly and mostly appending, I may want an append arena for it. If another application wants a different access pattern, it can use a different layout. If one application wants one kind of file-allocation table and another wants a different one, I want to be able to do that too.

This is not really separate from the representation work elsewhere here.

In [Rotations and hyperplanes](rotations-and-hyperplanes.md), the same mathematical object can have several concrete carriers. A multiply indexed vector makes the connection even more obvious: once it is stored, the choice of indices, strides, contiguous directions, materialized views, and transformations is also a storage-layout decision.

The same thing happens lower down. [Making programs smaller and faster](smaller-faster-programs.md) already asks what happens when the compiler owns the descent all the way to bytes and machine instructions. Once I am [writing an easy to read programming language](easy-to-read-programming-language.md) that can also lower directly to machine code, storage decisions eventually become address calculations and instructions. I want the map between the mathematical object and those addresses to be visible enough to choose.

The [semantic operating-system work](semantic-operating-system.md) reaches the same problem from another direction. IB and Pensieve want durable objects that can be reached through many indexes instead of forcing one hierarchy to be the truth. [Contextual find and replace](contextual-find-and-replace.md) uses those indexes as different ways to retrieve the same underlying thing. [FPGA grep](fpga-grep.md) asks a related question about whether a better index can avoid reading most of the data in the first place.

So I do not want "the filesystem" to become another universal representation that everything has to obey.

A general-purpose filesystem is useful. So are ordinary files and directories. But if an application has a storage pattern that is simple enough to describe directly, I want to be able to give that application the structure it actually needs.

That might mean an append arena for fast incoming data, several indexes over one body of data, an application-specific allocation table, or something else entirely.

The storage layout is part of the program design.
